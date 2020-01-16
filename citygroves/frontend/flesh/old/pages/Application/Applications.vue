<template>
  <div class="content">
    <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">
      <nav-tabs-card>
        <template slot="content">
          <span class="md-nav-tabs-title">Filter:</span>
          <md-tabs class="md-success" md-alignment="left">
            <md-tab id="pending" md-label="Pending" md-icon="timer">
              <app-table :applications="this.pending"/>
            </md-tab>
            <md-tab id="finalised" md-label="Finalised" md-icon="done">
              <app-table :applications="this.finalised"/>
            </md-tab>
            <md-tab id="removed" md-label="Removed" md-icon="delete">
              <app-table :applications="this.finalised"/>
            </md-tab>
          </md-tabs>
        </template>
      </nav-tabs-card>
    </div>
  </div>
</template>

<script lang="ts">
    import NavTabsCard from "@components/Cards/NavTabsCard";
    import AppTable from "./AppTable.vue";
    import {Manager} from "@/apis/manager";

    export default {
        data(): Object {
            return {
                loading: false,
                pending: [],
                finalised: [],
            }
        },
        components: {
            AppTable,
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
                  this.pending.push( {name: `${a.getTitle()}`, id: a.id})
                }
                this.loading = false;
            },
        }
    };
</script>
