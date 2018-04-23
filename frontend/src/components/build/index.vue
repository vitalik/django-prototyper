<template>
    <div>
        <div class="heading">
            <div class="container-fluid">
                <h2>Build</h2>
            </div>
        </div>

        <div class="container-fluid">
            <button @click="on_buld_click" class="btn btn-danger">RUN</button>

            <div v-if="show_complete" class="mt-2">
                <span v-if="build_success" class="text-success">Build success</span>
                <span v-else class="text-danger">Build failed</span>
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

export default {
    name: 'build',
    data() {
        return {
            show_complete: false,
            build_success: false,
            logs: []
        }
    },
    methods: {
        on_buld_click() {
            this.show_complete = false
            this.logs = []
            
            API.build().then((response)=>{
                this.logs = response.data.logs
                this.show_complete = true
                this.build_success = response.data.success
            })
        }
    }
}

</script>
