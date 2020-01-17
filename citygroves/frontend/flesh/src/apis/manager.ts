import axios from 'axios';
import {Config} from '@/config'
import * as url from "url";


class ApiObject {
    apiInterface: ApiInterface;

    constructor(apiInterface: ApiInterface, payload: Object) {
        this.apiInterface = apiInterface;
        for (const [name, value] of Object.entries(payload)) {
            this[name] = value;
        }
    }

    save(exclude?: Array<string>) {
        this.apiInterface.update(this, exclude);
    }
}

export class Address extends ApiObject {
    raw_address: String;
    street_line1: String;
    street_line2: String;
    street_line3: String;
    city: String;
    state: String;
    post_code: String;
    country: String;
}

export class Person extends ApiObject {
    first_name: String;
    middle_names: String;
    last_name: String;
    email: String;
    phone: String;
    dob: Date;
}

export class Tenant extends ApiObject {
    person: Person;
    room: Room;
    lease_start: Date;
    lease_end: Date;
    str_repr: String;

    getTitle(): String {
        return `${this.str_repr} U${this.room.unit.number}R${this.room.number}`
    }
}


export class Referrer extends ApiObject {
    first_name: String;
    last_name: String;
    email: String;
    phone: String;
    address: Address;
    dob: Date;
}

export class Unit extends ApiObject {
    number: Number
}

export class Room extends ApiObject {
    number: Number;
    unit: Unit;
}


export class Application extends ApiObject {
    apiInterface: ApiInterface;

    id: Number;
    person: Person;
    room: Room;
    current_address: Address;
    number_of_ppl_to_move_in: Number;
    move_in_date: Date;
    guarantor_will_pay: Boolean;
    is_employed: Boolean;
    centerlink_will_pay: Number;
    have_sufficient_funds: Boolean;
    is_local_student: Boolean;
    is_international_student: Boolean;
    is_young_professional: Boolean;
    referrers: Array<Referrer>;
    digital_signature: String;

    getTitle(): String {
        return `${this.person.first_name} ${this.person.last_name} U${this.room.unit.number}R${this.room.number}`
    }

    save() {
        super.save(["person", "room", "current_address", "referrers"]);
    }

    getLease() {
        axios({
            url: url.resolve(this.apiInterface.url, String(`${this.id}/getlease/`)),
            method: 'GET',
            responseType: 'blob',
        }).then((response) => {
            var fileURL = window.URL.createObjectURL(new Blob([response.data]));
            var fileLink = document.createElement('a');
            fileLink.href = fileURL;
            fileLink.setAttribute('download', `${this.getTitle().replace(/\s/g, "")}.pdf`);
            document.body.appendChild(fileLink);
            fileLink.click();
        });
    }
}

class ApiInterface {
    manager: Manager;
    ApiObjectType;
    url: string;

    constructor(manager: Manager, ApiObjectType, endpoint: string) {
        this.manager = manager;
        this.url = url.resolve(this.manager.apiUrl, endpoint);
        this.ApiObjectType = ApiObjectType;
    }

    getAll(): Array<Application> {
        return axios.get(this.url).then(req => {
            let applications: Array<Application> = [];
            for (const a of req.data) {
                applications.push(new this.ApiObjectType(this, a));
            }
            return applications;
        });
    }

    get(id: Number): Application {
        return axios.get(url.resolve(this.url, String(id))).then(req => {
            return new this.ApiObjectType(this, req.data);
        });
    }

    update(apiObject, exclude: Array<string> = []): Application {
        let payload = Object.assign({}, apiObject);
        delete payload.apiInterface;

        for (const excl of exclude) {
            delete payload[excl];
        }

        return axios.patch(url.resolve(this.url, String(payload.id) + "/"), payload);
    }
}

export class Manager {
    apiUrl: string;
    applications: ApiInterface;
    people: ApiInterface;
    tenants: ApiInterface;
    addresses: ApiInterface;
    referrer: ApiInterface;

    constructor() {
        this.apiUrl = Config.managerApiUrl;
        this.applications = new ApiInterface(this, Application, "applications/");
        this.people = new ApiInterface(this, Person, "people/");
        this.tenants = new ApiInterface(this, Tenant, "tenants/");
        this.addresses = new ApiInterface(this, Address, "addresses/");
        this.referrer = new ApiInterface(this, Referrer, "referrers/");
    }
}
