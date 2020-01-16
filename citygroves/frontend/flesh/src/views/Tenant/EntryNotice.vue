<template>
  <Card title="Tenants">
    <v-tabs>
      <v-tab href="#current">
        Current
      </v-tab>

      <v-tab href="#past">
        Past
        <v-icon>mdi-phone</v-icon>
      </v-tab>

      <v-tab-item value="current">
        <Table ref="currentTenantsTable" :tenants="current"/>
      </v-tab-item>

      <v-tab-item value="past">
        <v-card flat>
          <v-card-text>
            Test3
          </v-card-text>
        </v-card>
      </v-tab-item>

    </v-tabs>

    <template #actions>
      <v-btn color="success" @click="handleEntryNotice">Entry notice</v-btn>
      <v-btn color="success" @click="handleNoticeToLeave">Notice to leave</v-btn>
      <v-btn color="success" @click="handleConditionreport">Condition report</v-btn>
    </template>
  </Card>
</template>

<script lang="ts">
    import {Manager} from "@/apis/manager"
    import Table from "./Table.vue";
    import Card from "@/components/Cards/Card.vue"

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
            Card
        },
        async created() {
            await this.refresh();
        },
        methods: {
            async refresh() {
                this.loading = true;
                let manager = new Manager();
                let tenants = await manager.tenants.getAll();
                this.current = tenants;
                this.loading = false;
            },
            handleEntryNotice() {
              let selected = this.$refs.currentTenantsTable.selected;
              let a = 1;
            },
            handleNoticeToLeave() {

            },
            handleConditionreport() {

            }
        }
    };
</script>
