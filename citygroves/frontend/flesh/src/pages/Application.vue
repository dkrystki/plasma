<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">{{this.application.getTitle()}}</h4>
            <p class="category">Here is a subtitle for this table</p>
          </md-card-header>
          <md-card-content>
            <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="firstname"
            :rules="nameRules"
            :counter="10"
            label="First name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="lastname"
            :rules="nameRules"
            :counter="10"
            label="Last name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
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

<script lang="ts">
    import {Manager} from "@/apis/manager"

    export default {
        data(): Object {
            return {
                loading: false,
                application: [],
            }
        },
        components: {},
        async created() {
            this.refresh();
        },
        methods: {
            async refresh() {
                this.loading = true;
                let manager = new Manager();
                this.application = await manager.applications.get(Number(this.$route.params.id));
                let a = 1;
            },
        }
    };
</script>

