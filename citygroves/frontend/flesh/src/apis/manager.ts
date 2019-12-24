import axios from 'axios';
import {Config} from '@/config'
import App from "../App.vue";


class Address {
    raw_address: String;
    street_line1: String;
    street_line2: String;
    street_line3: String;
    city: String;
    state: String;
    post_code: String;
    country: String;
}

class Person {
    apiInterface: ApiInterface;

    first_name: String;
    last_name: String;
    email: String;
    phone: String;
    dob: Date;

    constructor(apiInterface: ApiInterface, payload: Object) {
        this.apiInterface = apiInterface;
        for (const [name, value] of Object.entries(payload)) {
            this[name] = value;
        }
    }

    save() {
        this.apiInterface.update(this);
    }
}


class Referrer {
    first_name: String;
    last_name: String;
    email: String;
    phone: String;
    address: Address;
    dob: Date;
}

class Unit {
    number: Number
}

class Room {
    number: Number;
    unit: Unit;
}


class Application {
    apiInterface: ApiInterface;

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
    constructor(apiInterface: ApiInterface, payload: Object) {
        this.apiInterface = apiInterface;
        for (const [name, value] of Object.entries(payload)) {
            this[name] = value;
        }
    }
}

class ApiInterface {
    manager: Manager;
    ApiObjectType;
    endpoint: String;

    constructor(manager: Manager, ApiObjectType, endpoint: String) {
        this.manager = manager;
        this.endpoint = endpoint;
        this.ApiObjectType = ApiObjectType;
    }

    getAll(): Array<Application> {
        return axios.get(`${this.manager.apiUrl}${this.endpoint}`).then(req => {
            let applications: Array<Application> = [];
            for(const a of req.data) {
                applications.push(new this.ApiObjectType(this, a));
            }
            return applications;
        });
    }

    get(id: Number): Application {
        return axios.get(`${this.manager.apiUrl}${this.endpoint}${id}/`).then(req => {
            return new this.ApiObjectType(this, req.data);
        });
    }
    update(apiObject): Application {
        let payload = Object.assign({}, apiObject);
        delete payload.apiInterface;

        return axios.put(`${this.manager.apiUrl}${this.endpoint}${payload.id}/`, payload);
    }
}

export class Manager {
    apiUrl: string;
    applications: ApiInterface;
    people: ApiInterface;

    constructor() {
        this.apiUrl = Config.managerApiUrl;
        this.applications = new ApiInterface(this, Application, "applications/");
        this.people = new ApiInterface(this, Person, "people/");
    }
}
