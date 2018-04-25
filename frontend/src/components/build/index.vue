<template>
    <div>
        <div class="heading">
            <div class="container-fluid">
                <h2>Build</h2>
            </div>
        </div>

        <modal v-show="build_warning_popup" title="Build" @close="build_warning_popup=false">
            <p>
                You are about to build your project.
            </p>
            <p>
                WARNING: this process <strong>will remove all contents</strong> of your project directory (previoius build):
                <br>
                <code>{{build_path}}</code>
            </p>
            <p>
                This action cannot be undone.
            </p>
            <hr>
            <button @click="on_buld_click" class="btn btn-danger">Yes, Build!</button>
            <button @click="build_warning_popup=false" class="btn btn-light">Cancel</button>
        </modal>

        <div class="container-fluid">
            <button @click="build_warning_popup=true" v-if="!build_in_progress" class="btn btn-success">Build again</button>

            <div v-if="show_complete" class="mt-2">
                <div v-if="build_success">
                    <span class="text-success">Build success</span>
                    <p>Now you can check your project:</p>

                    <div class="p-1" style="background-color: #eee; max-width: 400px;">
                        <code>
                            cd {{build_path}}<br>
                        </code>

                        <code>python3 -m venv .env   &nbsp; &nbsp;</code>
                        <span class="text-muted"># optional</span><br>

                        <code>source .env/bin/activate</code>
                        <span class="text-muted"># optional</span><br>

                        <code>
                            pip install -r requirements.txt<br>
                            ./manage.py migrate --run-syncdb<br>
                            ./manage.py runserver
                        </code>
                    </div>

                </div>
                <span v-else class="text-danger">Build failed</span>
            </div>

            <div v-if="build_in_progress">
                Build in progress. Please wait...
            </div>
            
            <table v-if="logs.length > 0" class="table table-sm mt-2" style="font-size: 0.7rem;">
                <thead>
                    <th>time</th>
                    <th style="width: 80%">message</th>
                </thead>
                <tbody>
                    <tr v-for="r in logs" :class="{'text-danger': r.level == 'ERROR', 'text-warning': r.level == 'WARNING'}">
                        <td>{{ r.time }}</td>
                        <td><samp style="white-space: pre;">{{ r.message }}</samp></td>
                    </tr>
                </tbody>
            </table>
        
        </div>

    </div>
</template>

<script>

import API from '../../backend'
import { store } from '../../store'
import Modal from '../utils/Modal'

export default {
    name: 'build',
    data() {
        return {
            show_complete: false,
            build_warning_popup: false,
            build_in_progress: false,
            build_success: false,
            logs: []
        }
    },
    computed: {
        build_path() {
            return store.project.path + '/' + store.project.name
        }
    },
    mounted() {
        this.build_warning_popup = true
    },
    methods: {
        on_buld_click() {
            this.show_complete = false
            this.build_in_progress = true
            this.build_warning_popup = false
            this.logs = []
            
            API.build().then((response)=>{
                this.logs = response.data.logs
                this.show_complete = true
                this.build_in_progress = false
                this.build_success = response.data.success
            })
        }
    },
    components: {
        Modal,
    }
}

</script>
