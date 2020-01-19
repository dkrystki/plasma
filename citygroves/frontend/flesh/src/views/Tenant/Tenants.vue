<template>
  <Card title="Tenants">
    <v-tabs>
      <v-tab href="#current">
        <v-icon>done_outline</v-icon>

        Current
      </v-tab>

      <v-tab href="#past">
        <v-icon>history</v-icon>
        Past
      </v-tab>

      <v-tab-item value="current">
        <Table ref="currentTenantsTable" @selection-changed="onSelectionChanged" :tenants="current"/>
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
      <v-btn ref="entry_notice_btn" color="success" disabled @click="handleEntryNotice">Entry notice</v-btn>
      <v-btn ref="notice_to_leave" color="success" disabled @click="handleNoticeToLeave">Notice to leave</v-btn>
      <v-btn ref="condition_report" color="success" disabled @click="handleConditionreport">Condition report</v-btn>
    </template>
  </Card>
</template>

<script lang="ts">
    import {api, Tenant} from "@/apis/backend";
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
                let tenants = await api.tenants.getAll();
                this.current = tenants;
                this.loading = false;
            },
            onSelectionChanged(items: Array<Tenant>) {

                this.$refs["entry_notice_btn"].disabled = !(items.length);
                this.$refs["notice_to_leave"].disabled = !(items.length);
                this.$refs["condition_report"].disabled = !(items.length);
            },
            handleEntryNotice() {
                let selected = this.$refs.currentTenantsTable.selected;
                this.$store.commit('tenants/setSelectedTenants', selected);
                this.$router.push({name: "EntryNotice"});
            },
            handleNoticeToLeave() {

            },
            handleConditionreport() {

            }
        }
    };
</script>
