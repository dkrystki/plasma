import axios from 'axios';

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


class Application {
    person: Person;
    unit_number: Number;
    room_number: Number;
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
}


class Applications {
    manager: Manager;

    constructor(manager: Manager) {
        this.manager = manager;
    }

    // get_all(): Array<Application>{
    //   axios.get(`${this.manager.api_url}/applications/`)
    // }
}

export class Manager {
    api_url: string;
    applications: Applications;

    constructor(api_url: string) {
        this.api_url = api_url;
        this.applications = new Applications(this);
    }
}
