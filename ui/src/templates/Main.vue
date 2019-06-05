<template>
  <b-container fluid>
    <b-alert :show="dismiss_countDown" variant="primary" @dismissed="dismiss_countDown=0" @dismiss-count-down="countDownChanged">
      {{this.alert_message}}
    </b-alert>
    <b-row id="row-main">
          <!-- <img src="@/assets/reternal.png" id="sidebar-header-image"> -->
      <b-col xl="1" lg="1" md="1" sm="1" cols="1" id="col-sidebar">
        <hr>
        <b-nav vertical id="sidebar-nav" class="sidebar-nav-links">
          <b-nav-item class="nav-item">
            <b-link to="/hits" active-class="active">
              <span class="nav-item-icon"><font-awesome-icon icon="exclamation-triangle" /></span>
            </b-link>
          </b-nav-item>
          <b-nav-item class="nav-item">
            <b-link to="/snapshots" active-class="active">
              <span class="nav-item-icon"><font-awesome-icon icon="camera-retro" /></span>
            </b-link>
          </b-nav-item>
        </b-nav>
        <hr>
        <b-nav vertical id="sidebar-nav" class="sidebar-nav-links">
          <b-nav-item class="nav-item">
            <b-link to="/whitelist" active-class="active">
              <span class="nav-item-icon"><font-awesome-icon icon="heart" /></span>
            </b-link>
          </b-nav-item>
          <b-nav-item class="nav-item">
            <b-link to="/regex" active-class="active">
              <span class="nav-item-icon"><font-awesome-icon icon="text-width" /></span>
            </b-link>
          </b-nav-item>
          <b-nav-item class="nav-item">
            <b-link to="/fuzzy" active-class="active">
              <span class="nav-item-icon"><font-awesome-icon icon="percentage" /></span>
            </b-link>
          </b-nav-item>
        </b-nav>
      </b-col>

      <b-col id="col-main">
        <b-row id="row-navbar">
          <b-col cols="12">
           <b-navbar toggleable="md" type="light" variant="platinum" >
            <b-navbar-nav class="ml-auto">
              <b-nav-item-dropdown right>
                <template slot="button-content">
                <font-awesome-icon icon="cog" />
                </template>
                <b-dropdown-item @click="logout" href="#">Signout</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-navbar>
        </b-col>
      </b-row>

        <b-row id="row-content">
          <b-col cols="12" class="column-content">
            <transition>
              <router-view></router-view>
            </transition>
          </b-col>
        </b-row>

      </b-col>
    </b-row>
  </b-container>
</template>

<script>

import EventBus from '@/eventbus'

export default {
  name: 'Main',
  data () {
    return {
      selected_agents: this.$store.getters['selection/get_agents_detailed'],
      alert_message: '',
      alert_type: 'primary',
      dismiss_secs: 10,
      dismiss_countDown: 0,
      countDownChanged: false
    };
  },
  mounted () {
    EventBus.$on('showalert', alert_data => {
      var alert_variant = {
        400: 'primary',
        200: 'success'
      };
      this.alert_type = alert_variant[alert_data.status];
      this.alert_message = alert_data.data;
      this.show_alert();
    });
  },
  methods: {
    logout () { 
      this.$store.commit('auth/delete_refresh_token')
      this.$store.commit('auth/delete_access_token')
      this.$router.push('/login')
    },
    show_alert () {
      this.dismiss_countDown = this.dismiss_secs;
    }
  }
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Open+Sans');
@import "@/assets/style.scss";


#row-main {
  min-height: 100vh;
}

#col-sidebar {
  background-color: white;
  color: #8e8e8e;
  border-right-style: solid;
  border-right-width: 1px;
  border-right-color: #bbbbbb;
  max-width:90px;
  font-size: 22px;

  #sidebar-header-image {
    width: 100%;
  }

  .sidebar-nav-links {
    text-align:center;
  }
 
  .active {
    .nav-item-icon {
      color: #9e1d1d;
    }
  }

  .nav-item-title {
    margin-left: 10px;
  }
  a {
    color: #8e8e8e;
    &:hover {
      .nav-item-icon {
        color: #9e1d1d;
      }
    }
  }
}


#row-navbar {
  border-bottom: 1px;
  color: #e8e5e1;
  .navbar-nav {
    .nav-item {
      margin-left: 24px;
      margin-right: 20px;
      text-transform: uppercase;
      font-size: 20px;
      font-weight: 400;
      letter-spacing: 2px;
      .dropdown-item {
        font-size: 14px;
      }
    }
    .nav-link {
      color: #dddddd !important;
    }
  }
}

#row-content {
  min-height: 100vh;
  .column-content {
    margin-top: 50px;
    padding-left: 50px;
    padding-right: 50px;
  }
}

</style>
