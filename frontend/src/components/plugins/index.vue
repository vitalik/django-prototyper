<template>
    <div class="h-100 plugins">
        <div class="heading">
            <div class="container-fluid">
                <h2>Plugins</h2>
            </div>
        </div>

        <div class="container-fluid h-100">
            <div class="row h-100">
                <div class="col-4 h-100" style="border-right: 1px solid #EBEDF8;">
                    <h4>Installed plugins</h4>
                    <span v-if="plugins.length == 0">Nothing</span>

                    <div v-for="plugin in plugins" class="plugin-item">
                        <button @click="uninstall(plugin.name)" class="btn btn-link text-danger float-right pt-0 pb-0">uninstall</button>
                        <strong>{{ plugin.name }}</strong>
                        <p class="text-muted mb-1">{{ plugin.description }}</p>
                    </div>

                </div>
                <div class="col-8 h-100">
                    <h4>Discover</h4>
                    <discover @install="install" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import Discover from './Discover'
import API from '../../backend'


export default {
    name: 'plugins',
    computed:{
        plugins() {
            return store.project.plugins
        }
    },
    methods: {
        install(name, url) {
            //TODO: check if name not present alrready
            API.plugin_install(name, url).then((resp) => {
                store.plugins_install(resp.data.plugin)
            })
        },
        uninstall(name) {
            store.plugins_delete(name)
        }
    },
    components: {
        Discover,
    }
}

</script>
