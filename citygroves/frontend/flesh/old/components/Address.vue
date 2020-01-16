<template>
  <v-card>
    <v-card-title>
      <h4 class="title">Address</h4>
    </v-card-title>
    <md-card-content>
      <v-form>
        <v-row>
          <v-col cols="12" md="4">
            <md-field>
              <label>Street Line 1</label>
              <md-input v-model="street_line1" @change="onChange"/>
            </md-field>
          </v-col>
          <v-col cols="12" md="4">
            <md-field>
              <label>Street Line 2</label>
              <md-input v-model="street_line2" @change="onChange"/>
            </md-field>
          </v-col>
          <v-col cols="12" md="4">
            <md-field>
              <label>Street Line 3</label>
              <md-input v-model="street_line3" @change="onChange"/>
            </md-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="3">
            <md-field>
              <label>City</label>
              <md-input v-model="city" @change="onChange"/>
            </md-field>
          </v-col>
          <v-col cols="12" md="3">
            <md-field>
              <label>State</label>
              <md-input v-model="state" @change="onChange"/>
            </md-field>
          </v-col>
          <v-col cols="12" md="3">
            <md-field>
              <label>Post Code</label>
              <md-input v-model="post_code" @change="onChange"/>
            </md-field>
          </v-col>
          <v-col cols="12" md="3">
            <md-field>
              <label>Country</label>
              <md-input v-model="country" @change="onChange"/>
            </md-field>
          </v-col>
        </v-row>
      </v-form>
    </md-card-content>
  </v-card>
</template>
<script>
    import {Manager} from "../../src/apis/manager"

    let manager = new Manager();

    export default {
        name: "Address",
        props: {
            id: Number
        },
        data() {
            return {
                street_line1: "",
                street_line2: "",
                street_line3: "",
                city: "",
                state: "",
                post_code: "",
                country: "",
            }
        },
        async created() {
            this.refresh();
        },
        methods: {
            onChange() {
                this.address.street_line1 = this.street_line1;
                this.address.street_line2 = this.street_line2;
                this.address.street_line3 = this.street_line3;
                this.address.city = this.city;
                this.address.state = this.state;
                this.address.post_code = this.post_code;
                this.address.country = this.country;
                this.address.save();
            },
            async refresh() {
                this.loading = true;

                this.address = await manager.addresses.get(Number(this.id));

                this.street_line1 = this.address.street_line1;
                this.street_line2 = this.address.street_line2;
                this.street_line3 = this.address.street_line3;
                this.city = this.address.city;
                this.state = this.address.state;
                this.post_code = this.address.post_code;
                this.country = this.address.country;
            },
        }
    };
</script>

