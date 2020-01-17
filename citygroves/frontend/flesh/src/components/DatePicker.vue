<template>
  <v-menu
          v-model="menu"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
  >
    <template v-slot:activator="{ on }">
      <v-text-field
              v-model="date"
              :label="label"
              prepend-icon="event"
              @input="updateValue"
              v-on="on"
      >
      ></v-text-field>
    </template>
    <v-date-picker v-model="date" @input="updateValue"/>
  </v-menu>
</template>
<script>
    export default {
        name: "DatePicker",
        props: {
            label: { type: String, default: "" },
            value: String
        },
        data() {
            return {
                date: String,
                menu: false
            }
        },
        created() {
          this.date = this.value;
        },
        methods: {
            updateValue: function () {
                this.menu = false;
                this.$emit('input', this.date);
            }
        }
    };
</script>
