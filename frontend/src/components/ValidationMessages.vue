<template>
  <div v-for="validator in validators" :key="validator.name">
    <small
      class="invalid-feedback"
      v-if="field.$dirty && field[validator.name].$invalid"
    >
      {{ validator.message }}
    </small>
  </div>
  <small class="valid-feedback" v-if="field.$dirty && !field.$invalid">
    Everything is fine
  </small>
</template>

<script>
export default {
  name: "ValidationMessages",
  props: {
    field: {
      type: Object,
      required: true
    },
    validators: {
      type: Array,
      required: true
    }
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
