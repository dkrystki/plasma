<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">

        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Personal information</h4>
          </md-card-header>
          <md-card-content>
            <v-form>
                <v-row>
                  <v-col cols="12" md="6">
                    <md-field>
                      <label>First name</label>
                      <md-input v-model="first_name" @change="on_change"/>
                    </md-field>
                  </v-col>

                  <v-col cols="12" md="6">
                    <md-field>
                      <label>Last name</label>
                      <md-input v-model="last_name" @change="on_change"/>
                    </md-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" md="6">
                    <md-field>
                      <label>E-mail</label>
                      <md-input v-model="email" @change="on_change"/>
                    </md-field>
                  </v-col>

                  <v-col cols="12" md="3">
                    <md-field>
                      <label>Phone</label>
                      <md-input v-model="phone" @change="on_change"/>
                    </md-field>
                  </v-col>

                  <v-col cols="12" md="3">
                    <md-datepicker v-model="dob">
                      <label>DOB</label>
                    </md-datepicker>
                  </v-col>
                </v-row>
            </v-form>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
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
            on_change() {
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
