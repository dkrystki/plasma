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
              <v-container>
                <v-row>
                  <v-col cols="12" md="2">
                    <v-text-field v-model="first_name" label="First name" @change="on_change"/>
                  </v-col>

                  <v-col cols="12" md="2">
                    <v-text-field v-model="last_name" label="Last name" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="3">
                    <v-text-field v-model="email" label="E-mail" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="3">
                    <v-text-field v-model="phone" label="Phone" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="2">
                    <v-text-field v-model="dob" label="DOB" @change="on_change"/>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>
<script>
    import {Manager} from "@/apis/manager"
    let manager = new Manager();

    export default {
        name: "person",
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

