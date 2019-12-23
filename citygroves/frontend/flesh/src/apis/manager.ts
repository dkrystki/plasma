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
    first_name: String;
    last_name: String;
    email: String;
    phone: String;
    dob: Date;
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
    constructor(payload: Object) {
        for (const [name, value] of Object.entries(payload)) {
            this[name] = value;
        }
    }
}

class Applications {
    manager: Manager;

    constructor(manager: Manager) {
        this.manager = manager;
    }

    getAll(): Array<Application> {
        return axios.get(`${this.manager.api_url}applications/`).then(req => {
            let applications: Array<Application> = [];
            for(const a of req.data) {
                applications.push(new Application(a));
            }
            return applications;
        });
    }

    get(id: Number): Application {
        return axios.get(`${this.manager.api_url}applications/${id}/`).then(req => {
            return new Application(req.data);
        });
    }
}

export class Manager {
    api_url: string;
    applications: Applications;

    constructor() {
        this.api_url = Config.managerApiUrl;
        this.applications = new Applications(this);
    }
}
