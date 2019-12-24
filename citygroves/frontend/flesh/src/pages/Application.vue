<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">
        <md-card v-if="this.application !== null">
          <md-card-header data-background-color="green">
            <h4 class="title">{{this.application.getTitle()}}</h4>
          </md-card-header>
          <md-card-content>
            <Person :id="this.application.person.id"/>
            <Address :id="this.application.person.id"/>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
    import {Manager} from "@/apis/manager"
    import Person from "@/components/Person.vue"
    import Address from "@/components/Address.vue"

    export default {
        data(): Object {
            return {
                loading: false,
                application: null,
            }
        },
        components: {
            Person,
            Address
        },
        async created() {
            await this.refresh();
        },

        methods: {
            async refresh() {
                this.loading = true;
                let manager = new Manager();
                this.application = await manager.applications.get(Number(this.$route.params.id));
            },
        }
    };
</script>

