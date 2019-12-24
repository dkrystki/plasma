<template>
  <div class="content">
    <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">
      <nav-tabs-card>
        <template slot="content">
          <span class="md-nav-tabs-title">Tasks:</span>
          <md-tabs class="md-success" md-alignment="left">
            <md-tab id="tab-home" md-label="Bugs" md-icon="bug_report">
              <nav-tabs-table :applications="this.applications"></nav-tabs-table>
            </md-tab>

          </md-tabs>
        </template>
      </nav-tabs-card>
    </div>
  </div>
</template>

<script lang="ts">
    import {NavTabsTable, NavTabsCard} from "@components";
    import {Manager} from "@/apis/manager"

    export default {
        data(): Object {
            return {
                loading: false,
                applications: [],
            }
        },
        components: {
            NavTabsTable,
            NavTabsCard
        },
        async created () {
            this.refresh();
        },
        methods: {
            async refresh() {
                this.loading = true;
                let manager = new Manager();
                let applications = await manager.applications.getAll();
                for( let a of applications) {
                  this.applications.push( {name: `${a.getTitle()}`, id: a.id})
                }
                this.loading = false;
            },
        }
    };
</script>
