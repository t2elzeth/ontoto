<template>
  <label :for="label.for">
    <b>{{ label.text }}</b>
    <span
      class="char-counter"
      :class="{
        hide: !label.field.$model.length || !label.field.$invalid
      }"
    >
      {{ label.field.$model.length }}
    </span>
  </label>
</template>

<script>
export default {
  name: "FieldLabel",
  props: {
    label: {
      type: Object,
      required: true
    }
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
