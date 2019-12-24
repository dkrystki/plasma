<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">

        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Referrer</h4>
          </md-card-header>
          <md-card-content v-if="this.referrer !== null">
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
                </v-row>
              <v-row>
                <v-col cols="12" md="12">
                <Address :id="this.referrer.address.id"/>
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
    import {Manager} from "@/apis/manager"
    import Address from "@components/Address";

    let manager = new Manager();

    export default {
        name: "Referrer",
        components: {Address},
        props: {
            id: Number
        },
        data() {
            return {
                first_name: "",
                last_name: "",
                email: "",
                phone: "",
                referrer: null,
            };
        },
        async created() {
            this.refresh();
        },
        methods: {
            on_change() {
                this.referrer.first_name = this.first_name;
                this.referrer.last_name = this.last_name;
                this.referrer.email = this.email;
                this.referrer.phone = this.phone;
                this.referrer.save();
            },
            async refresh() {
                this.loading = true;
                this.referrer = await manager.referrer.get(Number(this.id));

                this.first_name = this.referrer.first_name;
                this.last_name = this.referrer.last_name;
                this.email = this.referrer.email;
                this.phone = this.referrer.phone;
            },
        }
    };
</script>
