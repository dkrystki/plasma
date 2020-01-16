<template>
  <v-card>
    <v-card-title>
      <h4 class="title">Address</h4>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field v-model="street_line1" label="Street Line 1" @change="onChange"/>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field v-model="street_line2" label="Street Line 2" @change="onChange"/>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field v-model="street_line3" label="Street Line 3" @change="onChange"/>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="3">
            <v-text-field v-model="city" label="City" @change="onChange"/>
          </v-col>
          <v-col cols="12" md="3">
            <v-text-field v-model="state" label="State" @change="onChange"/>
          </v-col>
          <v-col cols="12" md="3">
            <v-text-field v-model="post_code" label="Post Code" @change="onChange"/>
          </v-col>
          <v-col cols="12" md="3">
            <v-text-field v-model="country" label="Country" @change="onChange"/>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
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
            await this.refresh();
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

