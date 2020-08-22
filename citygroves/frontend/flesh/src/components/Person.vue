<template>
  <v-card v-if="person !== null">
    <p v-if="errors.length">
      <b>Please correct the following error(s):</b>
      <ul>
        <li v-for="error in errors">{{ error }}</li>
      </ul>
    </p>
    <v-card-title>
      <h4 class="title">Personal information</h4>
    </v-card-title>

    <v-card-text>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field v-model="first_name" label="First name" @change="onChange"/>
        </v-col>

        <v-col cols="12" md="6">
          <v-text-field v-model="last_name" label="Last Name" @change="onChange"/>
        </v-col>
      </v-row>
      <v-row>

        <v-col cols="12" md="6">
          <v-text-field v-model="email" label="E-mail" @change="onChange"/>
        </v-col>

        <v-col cols="12" md="3">
          <v-text-field v-model="phone" label="Phone" @change="onChange"/>
        </v-col>

        <v-col cols="12" md="3">
          <DatePicker v-model="dob" label="DOB"/>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
    import {api} from "@/apis/backend"
    import DatePicker from "@components/DatePicker";

    export default {
        name: "Person",
        props: {
            id: Number
        },
        components: {
          DatePicker
        },
        data() {
            return {
              errors: [],
                first_name: "",
                last_name: "",
                email: "",
                phone: "",
                dob: "",
                person: null
            };
        },

        async created() {
            this.refresh();
        },
        watch: {
            dob: function (val) {
                this.person.dob = val;
                this.person.save();
            }
        },
        methods: {
          checkForm: function () {
              this.errors = [];

              let reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/


              if (!this.person.first_name) {
                this.errors.push('First name required');
              }

              if (this.person.first_name.length > 30) {
                this.errors.push('First name too long');
              }

              if (this.person.first_name.length <= 1) {
                this.errors.push('First name too short');
              }

              if (!this.person.last_name) {
                this.errors.push('Last name required');
              }

              if (this.person.last_name.length <= 1) {
                this.errors.push('Last name too short');
              }

              if (this.person.last_name.length > 30) {
                this.errors.push('Last name too long');
              }

              if (!this.person.phone) {
                this.errors.push('Phone required');
              }

              if (this.person.phone.length < 8) {
                this.errors.push('Phone too short');
              }

              if (this.person.phone.length > 9) {
                this.errors.push('Phone too long');
              }

              if (!this.person.phone) {
                this.errors.push('DOB require');
              }

              if (!this.person.email) {
                this.errors.push('Email required');
              }

              if (this.person.email.length > 30) {
                this.errors.push('Email too long');
              }

              else if (!reg.test(this.person.email)) {
                this.errors.push('Please enter correct email');
              }

              return !this.erros;

            },
            onChange() {
                this.person.first_name = this.first_name;
                this.person.last_name = this.last_name;
                this.person.email = this.email;
                this.person.phone = this.phone;
                this.person.dob = this.dob;
                if (this.checkForm())
                  this.person.save();
            },
            async refresh() {
                this.loading = true;
                this.person = await api.people.get(Number(this.id));

                this.first_name = this.person.first_name;
                this.last_name = this.person.last_name;
                this.email = this.person.email;
                this.phone = this.person.phone;
                this.dob = this.person.dob;
            },
        }
    };
</script>
