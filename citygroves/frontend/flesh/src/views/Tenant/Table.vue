<template>
  <div>
    <v-text-field
            v-model="search"
            label="Search"
            item-key="name"
            single-line
            hide-details
            prepend-icon="search"
    ></v-text-field>
    <v-data-table
            v-model="selected"
            :headers="headers"
            :items="tenants"
            :search="search"
            :custom-filter="this.filter"
            show-select
    >
      <template #item.name="{ item }">
        <router-link :to="{ name: 'Tenant', params: { id: item.id }}">
          {{item.str_repr}}
        </router-link>
      </template>

      <template #item.room="{ item }">
        {{item.room.number}}
      </template>

      <template #item.unit="{ item }">
        {{item.room.unit.number}}
      </template>

      <template #item.leaseStart="{ item }">
        {{item.lease_start}}
      </template>

      <template #item.leaseEnd="{ item }">
        {{item.lease_end}}
      </template>
    </v-data-table>
  </div>
</template>

<script>
    export default {
        name: "Table",
        props: ["tenants"],
        data() {
            return {
                headers: [
                    {text: 'Tenant', value: 'name', sortable: true, filterable: true},
                    {text: 'Room', value: 'room', sortable: true},
                    {text: 'Unit', value: 'unit', sortable: true},
                    {text: 'Lease start', value: 'leaseStart', sortable: true},
                    {text: 'Lease end', value: 'leaseEnd', sortable: true},
                ],
                selected: [],
                search: '',
            };
        },
        methods: {
            filter(value, search, item) {
                return item.getTitle().toLowerCase().includes(search.toLowerCase());
            },
        }
    };
</script>

<style>
  .md-table {
    height: 680px;
  }

</style>
