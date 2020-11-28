<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="signUp">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr />

        <div class="form-field">
          <FieldLabel
            :label="getFieldLabelProps('email', 'Email', vuelidate.email)"
          />
          <input
            type="text"
            placeholder="Enter Email"
            v-model="vuelidate.email.$model"
            :class="getInputFieldValidationClasses(vuelidate.email)"
            id="email"
          />
          <ValidationMessages
            :field="vuelidate.email"
            :validators="[
              {
                name: 'required',
                message: 'Email cannot be blank'
              },
              {
                name: 'emailValidator',
                message: 'Enter a valid email'
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps('full_name', 'Full name', vuelidate.full_name)
            "
          />

          <input
            type="text"
            placeholder="Enter Full name"
            v-model="vuelidate.full_name.$model"
            :class="getInputFieldValidationClasses(vuelidate.full_name)"
            id="full_name"
          />
          <ValidationMessages
            :field="vuelidate.full_name"
            :validators="[
              {
                name: 'required',
                message: 'Full name cannot be blank'
              },
              {
                name: 'minLength',
                message: `Full name must be at least ${validators.minLength.fullname} characters long`
              },
              {
                name: 'alpha',
                message: `Full name must contain only letters`
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps('phone', 'Phone number', vuelidate.phone)
            "
          />
          <input
            type="text"
            placeholder="Enter phone number"
            v-model="vuelidate.phone.$model"
            :class="getInputFieldValidationClasses(vuelidate.phone)"
            id="phone"
          />
          <ValidationMessages
            :field="vuelidate.phone"
            :validators="[
              {
                name: 'required',
                message: 'Phone number cannot be blank'
              },
              {
                name: 'minLength',
                message: `Phone number must be at least ${validators.minLength.phone} characters long`
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps('password', 'Password', vuelidate.password)
            "
          />
          <input
            type="password"
            placeholder="Enter Password"
            v-model="vuelidate.password.$model"
            :class="getInputFieldValidationClasses(vuelidate.password)"
            id="password"
          />
          <ValidationMessages
            :field="vuelidate.password"
            :validators="[
              {
                name: 'required',
                message: 'Password cannot be blank'
              },
              {
                name: 'minLength',
                message: `Password must be at least ${validators.minLength.password} characters long`
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps(
                'password2',
                'Repeat password',
                vuelidate.password2
              )
            "
          />
          <input
            type="password"
            placeholder="Repeat your password"
            v-model="vuelidate.password2.$model"
            :class="getInputFieldValidationClasses(vuelidate.password2)"
            id="password2"
          />
          <ValidationMessages
            :field="vuelidate.password2"
            :validators="[
              {
                name: 'required',
                message: 'Password cannot be blank'
              },
              {
                name: 'sameAsPassword',
                message: 'Your passwords did not match'
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps(
                'description',
                'Description',
                vuelidate.description
              )
            "
          />
          <input
            type="text"
            placeholder="Enter Description"
            v-model="vuelidate.description.$model"
            :class="getInputFieldValidationClasses(vuelidate.description)"
            id="description"
          />
          <ValidationMessages
            :field="vuelidate.description"
            :validators="[
              {
                name: 'required',
                message: 'Description cannot be blank'
              },
              {
                name: 'minLength',
                message: `Description must be at least ${validators.minLength.description} characters long`
              },
              {
                name: 'maxlength',
                message: `Description must be at max ${validators.maxLength.description} characters long`
              }
            ]"
          />
        </div>

        <button type="submit" class="register-btn">Sign Up</button>
        <p class="agreement">
          By creating an account you agree to our
          <a href="#">Terms & Privacy</a>.
        </p>
      </div>

      <div class="container signin">
        <p>Already have an account? <a href="#">Sign in</a>.</p>
      </div>
    </form>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ValidationMessages from "@/components/ValidationMessages";
import FieldLabel from "@/components/FieldLabel";

import { ref } from "vue";
// import axios from "axios";
// import { ref } from "vue";
import {
  email as emailValidator,
  minLength,
  required,
  sameAs,
  maxLength,
  alpha
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";

// import { urls } from "@/utils/api";
import {
  getInputFieldValidationClasses,
  getFieldLabelProps,
  validators
} from "@/utils/forms";

export default {
  name: "SignUp",
  components: {
    Navbar,
    Sidebar,
    ValidationMessages,
    FieldLabel
  },
  setup() {
    const signUpFormData = ref({
      email: "",
      full_name: "",
      phone: "",
      password: "",
      password2: "",
      description: ""
    });

    const rules = {
      email: {
        required,
        emailValidator
      },
      password: {
        required,
        minLength: minLength(validators.minLength.password)
      },
      password2: {
        required,
        sameAsPassword: sameAs(function() {
          return signUpFormData.value.password;
        })
      },
      full_name: {
        required,
        alpha,
        minLength: minLength(validators.minLength.fullname)
      },
      phone: {
        required,
        minLength: minLength(validators.minLength.phone)
      },
      description: {
        required,
        maxlength: maxLength(validators.maxLength.description),
        minLength: minLength(validators.minLength.description)
      }
    };

    const vuelidate = useVuelidate(rules, signUpFormData);

    function signUp() {
      console.log("FORM HAS BEEN SUBMITTED");

      vuelidate.value.$touch();
      console.log(signUpFormData.value.password);
      console.log(vuelidate.value.password2.$model);
      console.log(vuelidate.value.password2.sameAsPassword.$invalid);

      // if (vuelidate.value.$invalid) {
      //   console.log("DATA IS INVALID");
      //   return;
      // }
      // console.log("Data is valid");
      // axios
      //   .post(urls.signUp, signUpFormData)
      //   .then(res => console.log(res.data))
      //   .catch(err => console.log(err));
    }

    return {
      signUpFormData,
      signUp,
      vuelidate,
      getInputFieldValidationClasses,
      getFieldLabelProps,
      validators
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
