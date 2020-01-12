<template>
  <md-card>
    <md-card-content>
      <Table :tenants="this.current"/>
    </md-card-content>

  </md-card>

</template>

<script lang="ts">
    import {Manager} from "@/apis/manager"
    import Table from "./Table";

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
