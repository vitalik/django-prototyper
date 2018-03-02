import _ from 'lodash'
import Vue from 'vue'
import API from './backend'
import { guess_type }  from './django/guess'


export var store = {
    project: PROJECT_DATA,  // Global var (comes from html)

    save() {
        return API.save(this.project)
    },

    app_get (name) {
        return _.find(this.project.apps, {name})
    },
    app_add (name) {
        this.project.apps.push({
            name,
            models: [],
        })
    },
    app_delete(name) {
        let ind = _.findIndex(this.project.apps, {name:name})
        Vue.delete(this.project.apps, ind)
    },

    models_get(app_name, name) {
        let app = this.app_get(app_name)
        return _.find(app.models, {name})
    },
    models_add(app_name, name) {
        let app = this.app_get(app_name)
        app.models.push({
            name: name, 
            fields:[],
            admin: {'generate': true},
        })
    },
    models_delete(app_name, name) {
        let app = this.app_get(app_name)
        let ind = _.findIndex(app.models, {name:name})
        Vue.delete(app.models, ind)
    },
    models_keys() {
        let result = []
        _.each(_.sortBy(store.project.apps, ['name']), (app) => {
            _.each(app.models, (model) => result.push(app.name + '.' + model.name))
        })
        return result
    },

    fields_get(model, name) {
        return _.find(model.fields, {name})
    },

    fields_add(model_fields, name) {
        let res = guess_type(name, this)
        let fld = {
            name,
            'attrs': {},
            'type': res.type,
            'relation': res.relation,
        }
        model_fields.push(fld)
        return fld
    },
}
