<template>
  <div class="form-field">
    <FieldLabel :for="field.id" :text="field.labelText" :v$field="v$" />
    <InputField
      :type="field.type"
      :placeholder="field.placeholder"
      :v$field="v$"
      :id="field.id"
    />

    <ValidationMessages :v$field="v$" :validators="field.validators" />
  </div>
</template>

<script>
import FieldLabel from "@/components/FieldLabel";
import InputField from "@/components/InputField";
import ValidationMessages from "@/components/ValidationMessages";

export default {
  name: "FormField",
  components: {
    FieldLabel,
    InputField,
    ValidationMessages
  },
  props: {
    field: {
      type: Object,
      required: true
    },
    v$field: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    return {
      v$: props.v$field
    };
  }
};
</script>

<style scoped></style>
