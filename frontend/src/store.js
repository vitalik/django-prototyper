import _ from 'lodash'
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

    fields_get(model, name) {
        return _.find(model.fields, {name})
    },

    fields_add(model_fields, name) {
        let fld = {
            name,
            'type': guess_type(name),
        }
        model_fields.push(fld)
        return fld
    },
}
