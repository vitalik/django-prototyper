<template>
    <div>
        <input v-model="search_query" class="form-control mb-1" placeholder="Search...">
        <div :style="{opacity: show_loading ? 1 : 0}" class="progress mb-1" style="height: 4px;">
            <div class="progress-bar bg-warning progress-bar-striped progress-bar-animated" style="width: 100%;"></div>
        </div>
        
        <div v-for="item in results" class="card mb-1 p-1">
            <div>
                <button v-if="!is_installed(item.url)" @click="$emit('install', item.url)" class="btn btn-sm btn-primary float-right pt-0 pb-0">install</button>
                <strong>{{ item.url }}</strong>
                <p class="text-muted mb-1">Lorem ipsum dolor sit amet asd fasdfs daf </p>
            </div>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'
import API from '../../backend'
import { store } from '../../store'


export default {
    name: 'discover',
    data() {
        return {
            search_query: '',
            show_loading: false,
            results: []
        }
    },
    computed: {
        installed_plugins_urls() {
            return _.reduce(store.project.plugins, function(result, p) {
                result.push(p.url)
                return result
            }, [])
        }
    },
    mounted() {
        if (this.results.length == 0) {
            this.do_qeury(this)
        }
    },
    watch: {
        search_query() {
            this.do_qeury(this)
        }
    },
    methods: {
        do_qeury: _.debounce((component) => {
            component.show_loading = true
            API.plugin_search(component.search_query).then((resp) => {
                component.show_loading = false
                if (!resp.data.success) {
                    alert('Error: ' + resp.data.message)
                } else {
                    component.results = resp.data.results
                }
            }).catch((error) => {
                alert(error)
            });
        }, 300),

        is_installed(url) {
            return _.indexOf(this.installed_plugins_urls, url) != -1
        }
    }
}

</script>
