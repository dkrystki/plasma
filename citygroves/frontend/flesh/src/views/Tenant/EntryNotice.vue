<template>
  <Card title="Entry Notice">

    <v-data-table
            :headers="headers"
            :items="table_data"
    >
      <template #header.planned_on="{ header }">
        {{ header.text }}
        <DatePicker v-model="planned_on_header" @change="onPlannedOnChanged"/>
      </template>
      <template #item.planned_on="{ item }">
        <DatePicker v-model="item.planned_on"/>
      </template>

      <template #header.planned_time="{ header }">
        {{ header.text }}
        <v-text-field v-model="planned_time_header" @change="onPlannedTimeOnChanged"/>
      </template>
      <template #item.planned_time="{ item }">
        <v-text-field v-model="item.planned_time"/>
      </template>

      <template #header.is_inspection="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_inspection_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_inspection="{ item }">
        <v-checkbox v-model="item.is_inspection"/>
      </template>

      <template #header.is_cleaning="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_cleaning_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_cleaning="{ item }">
        <v-checkbox v-model="item.is_cleaning"/>
      </template>

      <template #header.is_repairs_or_maintenance="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_repairs_or_maintenance_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_repairs_or_maintenance="{ item }">
        <v-checkbox v-model="item.is_repairs_or_maintenance"/>
      </template>

      <template #header.is_pest_control="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_pest_control_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_pest_control="{ item }">
        <v-checkbox v-model="item.is_pest_control"/>
      </template>

      <template #header.is_showing_to_buyer="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_showing_to_buyer_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_showing_to_buyer="{ item }">
        <v-checkbox v-model="item.is_showing_to_buyer"/>
      </template>

      <template #header.is_valutation="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_valuation_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_valutation="{ item }">
        <v-checkbox v-model="item.is_valutation"/>
      </template>

      <template #header.is_fire_and_rescue="{ header }">
        {{ header.text }}
        <v-checkbox v-model="is_fire_and_rescue_header" @change="onCheckboxChanged($event, header.value)"/>
      </template>
      <template #item.is_fire_and_rescue="{ item }">
        <v-checkbox v-model="item.is_fire_and_rescue"/>
      </template>

      <template #item.actions="{ item }">
        <v-icon @click="downloadOne(item)">
          cloud_download
        </v-icon>
      </template>
    </v-data-table>
    <template #actions>
      <v-btn color="success" @click="onSendClick">Send All</v-btn>
      <v-btn color="success" @click="onDownloadAllClick">Download All</v-btn>
    </template>
  </Card>
</template>

<script lang="ts">
    import {api, EntryNotice} from "@/apis/backend"
    import Card from "@/components/Cards/Card.vue"
    import DatePicker from "@components/DatePicker";

    export default {
        name: "EntryNotice",
        data(): Object {
            return {
                headers: [
                    {text: 'Tenant', value: 'name', width: 200},
                    {text: 'R', value: 'room_number', sortable: false, width: 40},
                    {text: 'U', value: 'unit_number', sortable: false, width: 40},
                    {text: 'Planned on', value: 'planned_on', sortable: false, width: 120},
                    {text: 'Planned time', value: 'planned_time', sortable: false, width: 90},
                    {text: 'Inspection', value: 'is_inspection', sortable: false, width: 90},
                    {text: 'Cleaning', value: 'is_cleaning', sortable: false, width: 90},
                    {text: 'Repairs', value: 'is_repairs_or_maintenance', sortable: false, width: 90},
                    {text: 'Pest', value: 'is_pest_control', sortable: false, width: 90},
                    {text: 'Showing', value: 'is_showing_to_buyer', sortable: false, width: 90},
                    {text: 'Valutation', value: 'is_valutation', sortable: false, width: 90},
                    {text: 'Rescue', value: 'is_fire_and_rescue', sortable: false, width: 90},
                    {text: '', value: 'actions', sortable: false, width: 90},
                ],
                loading: false,
                planned_on_header: "2019-12-12",
                planned_time_header: "10am - 2pm",
                is_inspection_header: true,
                is_cleaning_header: false,
                is_repairs_or_maintenance_header: false,
                is_pest_control_header: false,
                is_showing_to_buyer_header: false,
                is_valuation_header: false,
                is_fire_and_rescue_header: false,
                tenants: [],
                table_data: [],
            }
        },
        components: {
            Card,
            DatePicker
        },
        created() {
            this.table_data = [];
            this.tenants = this.$store.state.tenants.selectedTenants;

            for (const t of this.tenants) {
                this.table_data.push(
                    {
                        tenant_id: t.id,
                        name: t.str_repr,
                        room_number: t.room.number,
                        unit_number: t.room.unit.number,
                        planned_on: "2019-12-12",
                        planned_time: "10am - 2pm",
                        is_inspection: this.is_inspection_header,
                        is_cleaning: false,
                        is_repairs_or_maintenance: false,
                        is_pest_control: false,
                        is_showing_to_buyer: false,
                        is_valutation: false,
                        is_fire_and_rescue: false,
                    }
                )
            }
        },
        methods: {
            onCheckboxChanged(event, name) {
                for (const row of this.table_data) {
                    row[name] = event;
                }
            },
            onPlannedOnChanged(value) {
                for (let [index, item] of this.table_data.entries()) {
                    this.table_data[index]["planned_on"] = value;
                }
            },
            onPlannedTimeOnChanged(value) {
                for (let [index, item] of this.table_data.entries()) {
                    this.table_data[index]["planned_time"] = value;
                }
            },
            onSendClick() {

            },
            onDownloadAllClick() {
                for (const te of this.table_data) {
                  this.downloadOne(te);
                }
            },
            async downloadOne(item) {
                let entry_notice = new EntryNotice();
                entry_notice.tenant = item.tenant_id;
                entry_notice.planned_on = item.planned_on;
                entry_notice.planned_time = item.planned_time;
                entry_notice.is_inspection = item.is_inspection;
                entry_notice.is_cleaning = item.is_cleaning;
                entry_notice.is_repairs_or_maintenance = item.is_repairs_or_maintenance;
                entry_notice.is_pest_control = item.is_pest_control;
                entry_notice.is_showing_to_buyer = item.is_showing_to_buyer;
                entry_notice.is_valutation = item.is_valutation;
                entry_notice.is_fire_and_rescue = item.is_fire_and_rescue;

                await api.entry_notices.create(entry_notice);
                entry_notice.getPdf();
            }
        },
    };
</script>
