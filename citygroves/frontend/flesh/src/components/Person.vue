<template>
  <v-card v-if="person !== null">
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
          <v-menu
                  v-model="menu2"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  lazy
                  transition="scale-transition"
                  offset-y
                  full-width
                  min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                      v-model="dob"
                      label="Picker without buttons"
                      prepend-icon="event"
                      readonly
                      v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="dob" @input="menu2 = false"></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
    import {Manager} from "../../src/apis/manager"

    let manager = new Manager();

    export default {
        name: "Person",
        props: {
            id: Number
        },
        data() {
            return {
                first_name: "",
                last_name: "",
                email: "",
                phone: "",
                dob: "",
                menu2: false,
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
            onChange() {
                this.person.first_name = this.first_name;
                this.person.last_name = this.last_name;
                this.person.email = this.email;
                this.person.phone = this.phone;
                this.person.dob = this.dob;
                this.person.save();
            },
            async refresh() {
                this.loading = true;
                this.person = await manager.people.get(Number(this.id));

                this.first_name = this.person.first_name;
                this.last_name = this.person.last_name;
                this.email = this.person.email;
                this.phone = this.person.phone;
                this.dob = this.person.dob;
            },
        }
    };
</script>
