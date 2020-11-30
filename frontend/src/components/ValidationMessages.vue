<template>
  <div v-for="validator in validators" :key="validator.name">
    <small
      class="invalid-feedback"
      v-if="v$.$dirty && v$[validator.name].$invalid"
    >
      {{ validator.message }}
    </small>
  </div>
  <small class="valid-feedback" v-if="v$.$dirty && !v$.$invalid">
    Everything is fine
  </small>
</template>

<script>
import {messages} from "@/utils/validators";

export default {
  name: "ValidationMessages",
  props: {
    v$field: {
      type: Object,
      required: true
    },
    fieldName: String,
  },
  setup(props) {
    return {
      v$: props.v$field,
      validators: messages[props.fieldName]
    };
  }
};
</script>

<style>
.invalid-feedback {
  color: red;
}

.valid-feedback {
  color: #00c700;
}
</style>
