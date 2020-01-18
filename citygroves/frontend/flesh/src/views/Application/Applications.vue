<template>
  <Card title="Applications">
    <v-tabs>
      <v-tab href="#tab-1">
        <v-icon>hourglass_empty</v-icon>
        Pending
      </v-tab>

      <v-tab href="#tab-2">
        <v-icon>history</v-icon>
        Past
      </v-tab>

      <v-tab href="#tab-3">
        <v-icon>delete</v-icon>
        Deleted
      </v-tab>

      <v-tab-item value="tab-1">
        <Table :applications="pending"/>
      </v-tab-item>

      <v-tab-item value="tab-2">
        <v-card flat>
          <v-card-text>
            Test2
          </v-card-text>
        </v-card>
      </v-tab-item>

      <v-tab-item value="tab-3">
        <v-card flat>
          <v-card-text>
            Test3
          </v-card-text>
        </v-card>
      </v-tab-item>

    </v-tabs>
  </Card>

</template>

<script lang="ts">
    import Table from "./Table.vue";
    import {Manager} from "@/apis/manager";
    import Card from "@/components/Cards/Card.vue"

    export default {
        data(): Object {
            return {
                loading: false,
                pending: [],
                finalised: [],
            }
        },
        components: {
            Table,
            Card
        },
        async created() {
            this.refresh();
        },
        methods: {
            async refresh() {
                this.loading = true;
                let manager = new Manager();
                let applications = await manager.applications.getAll();
                for (let a of applications) {
                    this.pending.push({name: `${a.getTitle()}`, id: a.id})
                }
                this.loading = false;
            },
        }
    };
</script>
