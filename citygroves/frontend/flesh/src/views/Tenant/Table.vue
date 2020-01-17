<template>
  <div>
    <v-text-field
            v-if="searchable"
            v-model="search"
            label="Search"
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
            item-key="str_repr"
            :show-select="selectable"
    >
      <template #item.name="{ item }">
          <router-link :to="{ name: 'Tenant', params: { id: item.id }}">
          {{ item.str_repr }}
        </router-link>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
    export default {
        name: "Table",
        props: {
            tenants: Array,
            selectable: {type: Boolean, default: true},
            searchable: {type: Boolean, default: true}
        },
        data() {
            return {
                headers: [
                    {text: 'Tenant', value: 'name', filterable: true, width: 300},
                    {text: 'Room', value: 'room.number', width: 100},
                    {text: 'Unit', value: 'room.unit.number', width: 100},
                    {text: 'Lease start', value: 'lease_start', width: 200},
                    {text: 'Lease end', value: 'lease_end', width: 200},
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
