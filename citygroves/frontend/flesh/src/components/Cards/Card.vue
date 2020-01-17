<template>
  <div>
    <v-card>
      <v-toolbar color="green" dark>
        <v-card-title>
          {{ this.title }}
        </v-card-title>
      </v-toolbar>

      <v-card-text>
        <slot/>
      </v-card-text>

      <v-card-actions>
        <v-btn color="success" @click="goBack">Back</v-btn>
        <slot name="actions"/>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
    export default {
        props: {
            title: String,
        },
        methods: {
            goBack() {
                this.$router.go(-1);
            },
        },
    }
</script>

<style lang="scss">
  .v-card--material {
    &__header {
      &.v-card {
        border-radius: 4px;
      }
    }
  }
</style>
