import axios from 'axios';
import {Config} from '@/config'
import * as url from "url";


class ApiObject {
    api_interface: ApiInterface;
    id: Number;
    str_repr: string;

    /**
     * Patch an object
     * @param {exclude} exclude fields from patching.
     */
    save(exclude?: Array<string>) {
        this.api_interface.update(this, exclude);
    }

    async _getFile(url: string, filename: string) {
        let response = await axios({
            url: url,
            method: 'GET',
            responseType: 'blob',
        });

        var fileURL = window.URL.createObjectURL(new Blob([response.data]));
        var fileLink = document.createElement('a');
        fileLink.href = fileURL;
        fileLink.setAttribute('download', filename);
        document.body.appendChild(fileLink);
        fileLink.click();
    }
}

export class Address extends ApiObject {
    raw_address: string;
    street_line1: string;
    street_line2: string;
    street_line3: string;
    city: string;
    state: string;
    post_code: string;
    country: string;
}

export class Person extends ApiObject {
    first_name: string;
    middle_names: string;
    last_name: string;
    email: string;
    phone: string;
    dob: Date;
}

export class Tenant extends ApiObject {
    person: Person;
    room: Room;
    lease_start: Date;
    lease_end: Date;
    str_repr: string;

    getTitle(): string {
        return `${this.str_repr} U${this.room.unit.number}R${this.room.number}`
    }
}

export class EntryNotice extends ApiObject {
    tenant: Number;
    planned_on: Date;
    planned_time: string;
    is_inspection: Boolean;
    is_cleaning: Boolean;
    is_repairs_or_maintenance: Boolean;
    is_pest_control: Boolean;
    is_showing_to_buyer: Boolean;
    is_valutation: Boolean;
    is_fire_and_rescue: Boolean;
    details: string;

    getPdf() {
        this._getFile(url.resolve(this.api_interface.url, String(`${this.id}/?pdf/`)),
            `${this.str_repr}.pdf`);
    }

    send() {
        axios.post(url.resolve(this.api_interface.url, String(`${this.id}/send/`)));
    }
}

export class Referrer extends ApiObject {
    first_name: string;
    last_name: string;
    email: string;
    phone: string;
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
    api_interface: ApiInterface;

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
    digital_signature: string;

    getTitle(): string {
        return `${this.person.first_name} ${this.person.last_name} U${this.room.unit.number}R${this.room.number}`
    }

    save() {
        super.save(["person", "room", "current_address", "referrers"]);
    }

    getLease() {
        this._getFile(url.resolve(this.api_interface.url, String(`${this.id}/getlease/`)),
            `${this.getTitle().replace(/\s/g, "")}.pdf`);
    }
}

class ApiInterface {
    api: Api;
    ApiObjectType;
    url: string;

    constructor(api: Api, ApiObjectType, endpoint: string) {
        this.api = api;
        this.url = url.resolve(this.api.apiUrl, endpoint);
        this.ApiObjectType = ApiObjectType;
    }

    getAll(): Array<Application> {
        return axios.get(this.url).then(req => {
            let applications: Array<Application> = [];
            for (const obj of req.data) {
                let api_object = new this.ApiObjectType();
                api_object.api_interface = this;

                for (const [name, value] of Object.entries(obj)) {
                    api_object[name] = value;
                }
                applications.push(api_object);
            }
            return applications;
        });
    }

    async get(id: Number) {
        let response = await axios.get(url.resolve(this.url, String(id)));
        let api_object = new this.ApiObjectType();
        api_object.api_interface = this;
        for (const [name, value] of Object.entries(response.data)) {
                    api_object[name] = value;
                }

        return api_object;
    }

    update(apiObject: ApiObject, exclude: Array<string> = []) {
        let payload = Object.assign({}, apiObject);

        // Remove api_interface object so we don't send it to the backend
        delete payload.api_interface;

        for (const excl of exclude) {
            delete payload[excl];
        }

        axios.patch(url.resolve(this.url, String(payload.id) + "/"), payload);
    }

    async create(apiObject: ApiObject) {
        let payload = Object.assign({}, apiObject);
        let response = await axios.post(this.url, payload);
        apiObject.api_interface = this;
        apiObject.id = response.data.id;
        apiObject.str_repr = response.data.str_repr;
    }
}

class Api {
    apiUrl: string;
    applications: ApiInterface;
    people: ApiInterface;
    tenants: ApiInterface;
    addresses: ApiInterface;
    referrer: ApiInterface;
    entry_notices: ApiInterface;

    constructor() {
        this.apiUrl = Config.backend.apiUrl;
        this.applications = new ApiInterface(this, Application, "applications/");
        this.people = new ApiInterface(this, Person, "people/");
        this.tenants = new ApiInterface(this, Tenant, "tenants/");
        this.addresses = new ApiInterface(this, Address, "addresses/");
        this.referrer = new ApiInterface(this, Referrer, "referrers/");
        this.entry_notices = new ApiInterface(this, EntryNotice, "entry-notices/");
    }
}

export let api: Api = new Api();
