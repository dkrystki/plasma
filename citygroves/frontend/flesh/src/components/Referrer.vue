<template>
  <v-card v-if="this.referrer !== null">
    <v-card-title>
      <h4 class="title">Referrer</h4>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field v-model="first_name" label="First name" @change="onChange"/>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field v-model="last_name" label="Last name" @change="onChange"/>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field v-model="email" label="E-mail" @change="onChange"/>
          </v-col>

          <v-col cols="12" md="3">
            <v-text-field v-model="phone" label="Phone" @change="onChange"/>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="12">
            <Address :id="this.referrer.address.id"/>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </v-card>
</template>
<script>
    import {api} from "@/apis/backend"
    import Address from "./Address";

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
            await this.refresh();
        },
        methods: {
            onChange() {
                this.referrer.first_name = this.first_name;
                this.referrer.last_name = this.last_name;
                this.referrer.email = this.email;
                this.referrer.phone = this.phone;
                this.referrer.save();
            },
            async refresh() {
                this.loading = true;
                this.referrer = await api.referrer.get(Number(this.id));

                this.first_name = this.referrer.first_name;
                this.last_name = this.referrer.last_name;
                this.email = this.referrer.email;
                this.phone = this.referrer.phone;
            },
        }
    };
</script>
