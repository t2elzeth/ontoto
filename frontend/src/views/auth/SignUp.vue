<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="signUp">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr />

        <FormField :field="signUpFormData.email" :v$field="v$.email" />
        <FormField :field="signUpFormData.full_name" :v$field="v$.full_name" />
        <FormField :field="signUpFormData.phone" :v$field="v$.phone" />
        <FormField :field="signUpFormData.password" :v$field="v$.password" />
        <FormField :field="signUpFormData.password2" :v$field="v$.password2" />
        <FormField
          :field="signUpFormData.description"
          :v$field="v$.description"
        />

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
import FormField from "@/components/FormField";

import { ref } from "vue";
// import axios from "axios";
import {
  email,
  minLength,
  required,
  sameAs,
  maxLength,
  alpha
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";

// import { urls } from "@/utils/api";
import { success, error } from "@/utils/notifications";
import { validators, getStates } from "@/utils/forms";

export default {
  name: "SignUp",
  components: {
    Navbar,
    Sidebar,
    FormField
  },
  setup() {
    const signUpFormData = {
      email: {
        data: ref(""),
        id: "email",
        placeholder: "Enter email",
        labelText: "Email",
        validators: [
          {
            name: "required",
            message: "Email cannot be blank"
          },
          {
            name: "email",
            message: "Enter a valid email"
          }
        ]
      },
      full_name: {
        data: ref(""),
        id: "full_name",
        placeholder: "Enter Full name",
        labelText: "Full name",
        validators: [
          {
            name: "required",
            message: "Full name cannot be blank"
          },
          {
            name: "minLength",
            message: `Full name must be at least ${validators.minLength.fullname} characters long`
          },
          {
            name: "alpha",
            message: `Full name must contain only letters`
          }
        ]
      },
      phone: {
        data: ref(""),
        id: "phone",
        placeholder: "Enter Phone number",
        labelText: "Phone number",
        validators: [
          {
            name: "required",
            message: "Phone number cannot be blank"
          },
          {
            name: "minLength",
            message: `Phone number must be at least ${validators.minLength.phone} characters long`
          }
        ]
      },
      password: {
        data: ref(""),
        id: "password",
        placeholder: "Enter Password",
        labelText: "Password",
        type: "password",
        validators: [
          {
            name: "required",
            message: "Password cannot be blank"
          },
          {
            name: "minLength",
            message: `Password must be at least ${validators.minLength.password} characters long`
          }
        ]
      },
      password2: {
        data: ref(""),
        id: "password2",
        placeholder: "Repeat your password",
        labelText: "Repeat password",
        type: "password",
        validators: [
          {
            name: "required",
            message: "Password cannot be blank"
          },
          {
            name: "sameAs",
            message: "Your passwords did not match"
          }
        ]
      },
      description: {
        data: ref(""),
        id: "description",
        placeholder: "Enter Description",
        labelText: "Description",
        validators: [
          {
            name: "required",
            message: "Description cannot be blank"
          },
          {
            name: "minLength",
            message: `Description must be at least ${validators.minLength.description} characters long`
          },
          {
            name: "maxlength",
            message: `Description must be at max ${validators.maxLength.description} characters long`
          }
        ]
      }
    };

    const rules = {
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(validators.minLength.password)
      },
      password2: {
        required,
        sameAs: sameAs(signUpFormData.password.data, "")
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

    const v$ = useVuelidate(rules, getStates(signUpFormData));

    // function signUp() {
    // console.log("Data is valid");
    // axios
    //   .post(urls.signUp, signUpFormData)
    //   .then(res => console.log(res.data))
    //   .catch(err => console.log(err));
    // }

    function signUp() {
      // Validate data
      v$.value.$touch();

      // console.log(v$.value.password.$model);
      console.log(signUpFormData.value.full_name.data);
      console.log(v$.value.$invalid);
      // If data is invalid
      if (v$.value.$invalid) {
        error("Your data is invalid");
        return;
      }

      success("Your account has been successfully created");
    }

    return {
      signUp,
      signUpFormData,
      v$
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
