<template>
  <v-data-table
          :headers="headers"
          :items="applications"
  >
  <template #item.name="{ item }">
    <router-link :to="{ name: 'Application', params: { id: item.id }}">
      {{item.name}}
    </router-link>
    </template>
  </v-data-table>
</template>

<script>
    export default {
        name: "app-table",
        props: ["applications"],
        data() {
            return {
                headers: [
                    {text: 'Name', value: 'name'},
                ],
            };
        },
        methods: {
            // onSelect: function (items) {
            //     this.selected = items;
            // },
        }
    };
</script>

