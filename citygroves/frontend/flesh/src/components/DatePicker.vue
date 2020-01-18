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
              v-model="value"
              :label="label"
              prepend-icon="event"
              @input="updateValue"
              v-on="on"
      >
      ></v-text-field>
    </template>
    <v-date-picker v-model="value"
                   @input="updateValue"/>
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
                menu: false,
            }
        },
        methods: {
            updateValue: function () {
                this.menu = false;
                this.$emit('input', this.value);
                this.$emit('change', this.value);
            }
        }
    };
</script>
