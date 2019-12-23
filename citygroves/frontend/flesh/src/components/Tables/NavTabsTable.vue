<template>
  <div>
    <md-table v-model="applications" @md-selected="onSelect">
      <md-table-row
              slot="md-table-row"
              slot-scope="{ item }"
              md-selectable="multiple"
      >

        <md-table-cell>
          <router-link :to="{ name: 'ApplicationsDetails', params: { id: item.id }}">
          <div
                  class="md-list-item-router md-list-item-container md-button-clean dropdown"
          >{{item.name}}</div>
          </router-link>
        </md-table-cell>

        <md-table-cell>
          <md-button class="md-just-icon md-simple md-danger">
            <md-icon>close</md-icon>
            <md-tooltip md-direction="top">Close</md-tooltip>
          </md-button>
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
    export default {
        name: "nav-tabs-table",
        props: ["applications"],
        data() {
            return {
                selected: [],
            };
        },
        methods: {
            onSelect: function (items) {
                this.selected = items;
            },
        }
    };
</script>
