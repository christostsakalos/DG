<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/log-in" class="navbar-item"><strong>G Manager</strong></router-link>
      </div>
      <div class="navbar-menu">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">{{ $t("Dashboard") }}</router-link>
            <router-link to="/jobsheets" class="navbar-item">{{ $t("Jobsheets") }}</router-link>

                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          {{ $t("Finance") }}
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/invoices" class="navbar-item">{{ $t("Invoices") }}</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/invoices/add" class="navbar-item">{{ $t("Add Invoice") }}</router-link>
          </a>
        </div>
      </div>

                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
         {{ $t("Administration") }}
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/categories" class="navbar-item">{{ $t("Categories") }}</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/invoicesdelete" class="navbar-item">{{ $t("Invoices") }}</router-link>
          </a>
        </div>
      </div>



                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          {{ $t("General") }}
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/customers" class="navbar-item">{{ $t("Customers") }}</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/vehicles" class="navbar-item">{{ $t("Vehicles") }}</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/parts" class="navbar-item">{{ $t("Inventory") }}</router-link>
          </a>
        </div>
      </div>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/my-account" class="button is-light">{{ $t("My account") }}</router-link>
              </div>
            </div>
            <div class="navbar-item">
              <div class="buttons">
                <Logout></Logout>
              </div>
            </div>
          </template>

          <template v-else>

            <div class="navbar-item">
              <div class="buttons">
               <!--  <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link> -->
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </div>
            </div> 
          </template>
        </div>
      </div>
    </nav><Languages />
    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="content has-text-centered">Copyright Tsakal (c) 2021</p>
      
    </footer>
  </div>
</template>

<script>
  import axios from 'axios';
  import Logout from '../src/components/buttons/Logout';
  import {useI18n} from 'vue-i18n';
import Languages from '@/components/Languages.vue';
  export default {
    name: 'App',
    components: {
      Logout, Languages
    },

    setup(){
      const { t, locale} = useI18n();
      return { t, locale}
    },
    data(){
      const lang = localStorage.getItem('lang') || 'en';
      return{
        lang: lang
      }
    },

    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    methods:{
      handleChange(event){
        localStorage.setItem('lang', event.target.value);
        window.location.reload();
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
