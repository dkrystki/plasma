<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">

        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Address</h4>
          </md-card-header>
          <md-card-content>
            <v-form>
              <v-container>
                <v-row>
                  <v-col cols="12" md="2">
                    <v-text-field v-model="street_line1" label="Street Line 1" @change="on_change"/>
                  </v-col>

                  <v-col cols="12" md="2">
                    <v-text-field v-model="street_line2" label="Street Line 2" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="3">
                    <v-text-field v-model="street_line3" label="Street Line 3" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="3">
                    <v-text-field v-model="city" label="City" @change="on_change"/>
                  </v-col>
                  <v-col cols="12" md="2">
                    <v-text-field v-model="state" label="State" @change="on_change"/>
                  </v-col>`
                  <v-col cols="12" md="2">
                    <v-text-field v-model="post_code" label="Post Code" @change="on_change"/>
                  </v-col>`
                  <v-col cols="12" md="2">
                    <v-text-field v-model="country" label="Country" @change="on_change"/>
                  </v-col>`
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
        name: "address",
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
            on_change() {
                this.address.street_line1 = this.street_line1;
                this.address.street_line2 = this.street_line2;
                this.address.street_line3 = this.street_line3;
                this.address.city = this.city;
                this.address.state = this.state;
                this.address.save();
            },
            async refresh() {
                this.loading = true;

                this.address = await manager.people.get(Number(this.id));

                this.street_line1 = this.address.street_line1;
                this.street_line2 = this.address.street_line2;
                this.street_line3 = this.address.street_line3;
                this.city = this.address.city;
                this.state = this.address.state;
            },
        }
    };
</script>

