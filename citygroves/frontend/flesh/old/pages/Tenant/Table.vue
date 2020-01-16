<template>
    <md-table v-model="searched" md-sort="person.first_name" md-sort-order="asc" @md-selected="onSelect">
      <md-table-toolbar>
        <md-field md-clearable class="md-toolbar-section-end">
          <md-input placeholder="Search by name..." v-model="search" @input="searchOnTable" />
        </md-field>
      </md-table-toolbar>


      <md-table-empty-state
        md-label="No users found"
        :md-description="`No tenants found for this '${search}' query. Try a different search term or create a new user.`">
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" md-auto-select>
        <md-table-cell md-label="Tenant" md-sort-by="person.first_name">
          <router-link :to="{ name: 'Tenant', params: { id: item.id }}">
            <div class="md-list-item-router md-list-item-container md-button-clean dropdown">
              {{ item.str_repr }}
            </div>
          </router-link>
        </md-table-cell>

        <md-table-cell md-sort-by="room.number" md-label="Room">
          {{ item.room.number }}
        </md-table-cell>

        <md-table-cell md-sort-by="room.unit.number" md-label="Unit">
          {{ item.room.unit.number }}
        </md-table-cell>

        <md-table-cell md-sort-by="lease_start" md-label="Lease Start">
          {{ item.lease_start }}
        </md-table-cell>

        <md-table-cell md-sort-by="lease_end" md-label="Lease End">
          {{ item.lease_end }}
        </md-table-cell>
      </md-table-row>
    </md-table>
</template>

<script>
  const toLower = text => {
    return text.toString().toLowerCase()
  };
  const searchByName = (items, term) => {
    if (term) {
      return items.filter(item => toLower(item.getTitle()).includes(toLower(term)))
    }

    return items
  };
    export default {
        name: "Table",
        props: ["tenants"],
        data() {
            return {
                selected: [],
                searched: [],
                search: null,
            };
        },
        async created() {
             this.searched = await this.tenants;
        },
        methods: {
            onSelect: function (items) {
                this.selected = items;
            },
            async searchOnTable () {
        this.searched = searchByName(await this.tenants, this.search)
      }
        }
    };
</script>

<style>
  .md-table {
    height: 680px;
  }

</style>
