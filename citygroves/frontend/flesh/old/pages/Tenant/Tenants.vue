<template>
  <md-card>
    <md-card-content>
      <Table :tenants="this.current" ref="table"/>
    </md-card-content>
    <md-card-actions>
      <v-spacer/>
      <md-button class="md-primary" @click="downloadLease">Entry notice</md-button>
      <md-button class="md-primary" @click="goBack">Exit notice</md-button>
      <md-button class="md-primary" @click="downloadLease">Entry notice</md-button>
      <v-spacer/>
    </md-card-actions>
  </md-card>

</template>

<script lang="ts">
    import {Manager} from "@/apis/manager"
    import Table from "./Table.vue";

    export default {
        data(): Object {
            return {
                loading: false,
                current: [],
                finalised: [],
            }
        },
        components: {
            Table,
        },
        created() {
            this.refresh();
        },
        methods: {
            refresh() {
                this.loading = true;
                let manager = new Manager();
                let tenants = manager.tenants.getAll();
                this.current = tenants;
                this.loading = false;
            },
        }
    };
</script>
