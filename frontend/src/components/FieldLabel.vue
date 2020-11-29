<template>
  <label :for="for_id">
    <b>{{ text }}</b>
    <span
      class="char-counter"
      :class="{
        hide: !v$.$model.length || !v$.$invalid
      }"
    >
      {{ v$.$model.length }}
    </span>
  </label>
</template>

<script>
export default {
  name: "FieldLabel",
  props: {
    for: String,
    text: String,
    v$field: Object
  },
  setup(props) {
    return {
      v$: props.v$field,
      for_id: props.for
    };
  }
};
</script>

<style scoped lang="scss">
label {
  display: flex;
  justify-content: space-between;
  align-items: center;

  .char-counter {
    font-size: 12px;
  }

  .hide {
    display: none;
  }
}
</style>
