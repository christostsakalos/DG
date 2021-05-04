<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/log-in" class="navbar-item"><strong>G Manager</strong></router-link>
      </div>

      <div class="navbar-menu">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
            <router-link to="/jobsheets" class="navbar-item">Jobsheets</router-link>

                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          Finace
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/invoices" class="navbar-item">Invoices</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/invoices/add" class="navbar-item">Add Invoice</router-link>
          </a>
        </div>
      </div>

                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
         Administration
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/categories" class="navbar-item">Categories</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/invoicesdelete" class="navbar-item">Invoices</router-link>
          </a>
        </div>
      </div>



                  <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          General
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            <router-link to="/customers" class="navbar-item">Customers</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/vehicles" class="navbar-item">Vehicles</router-link>
          </a>
          <a class="navbar-item">
           <router-link to="/parts" class="navbar-item">Inventory</router-link>
          </a>
        </div>
      </div>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/my-account" class="button is-light">My account</router-link>
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
    </nav>
    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="content has-text-centered">Copyright Tsakal (c) 2021</p>
    </footer>
  </div>
</template>

<script>
  import axios from 'axios'
  import Logout from '../src/components/buttons/Logout'

  export default {
    name: 'App',
    components: {
      Logout
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
