<template>
    <div>
        <h2>Plugins</h2>
        <hr>

        <div class="row">
            <div class="col-4">
                <div class="card">
                    <div class="card-body">
                        <h4>Installed plugins</h4>
                        <span v-if="plugins.length == 0">Nothing</span>

                        <div v-for="plugin in plugins" class="card p-1 mb-1">
                            <div>
                                <button @click="uninstall(plugin.url)" class="btn btn-link text-danger float-right pt-0 pb-0">uninstall</button>
                                <strong>{{ plugin.title }}</strong>
                                <p class="text-muted mb-1">Lorem</p>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="col-8">
                <div class="card">
                    <div class="card-body">
                        <h4>Discover</h4>
                        <discover @install="install" />
                    </div>
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
        install(url) {
            API.plugin_install(url).then((resp) => {
                store.project.plugins.push(resp.data.plugin)
            })
        },
        uninstall(url) {
            store.plugins_delete(url)
        }
    },
    components: {
        Discover,
    }
}

</script>
