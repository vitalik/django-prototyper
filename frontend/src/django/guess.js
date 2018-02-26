import _ from 'lodash'



function guess_common_names(name) {
    if (_.startsWith(name, 'is_') || _.startsWith(name, 'has_') || _.startsWith(name, 'have_') || _.startsWith('allow_') || _.startsWith('can_'))
        return 'BooleanField'

    if (_.includes(name, 'slug'))
        return 'SlugField'

    if (_.includes(name, 'time'))
        return 'DateTimeField'

    if (_.includes(name, 'date'))
        return 'DateField'

    if (_.includes(name, 'duration'))
        return 'DurationField'

    if (_.includes(name, 'email'))
        return 'EmailField'

    if (_.endsWith(name, 'url'))
        return 'URLField'

    if (_.includes(name, 'file') || _.includes(name, 'pdf'))
        return 'FileField'

    if (_.includes(name, 'image') || _.includes(name, 'picture') || _.includes(name, 'photo') || _.includes(name, 'avatar'))
        return 'ImageField'

    if (_.includes(name, 'text') || _.includes(name, 'description') || _.includes(name, 'message') || _.includes(name, 'intro') || _.includes(name, 'content'))
        return 'TextField'
    
    return null
}

function guess_relational(name, store) {
    let model_names = _.keyBy(store.models_keys(), (key) => {
        return key.split('.')[1].toLowerCase()
    })
    if (model_names[name] !== undefined)
        return {type: 'ForeignKey', relation: model_names[name]}
    if (_.endsWith(name, 's')) {
        let m2m_name = name.slice(0, -1)
        if (model_names[m2m_name] !== undefined)
        return {type: 'ManyToManyField', relation: model_names[m2m_name]}
    }
    if (_.endsWith(name, 'ies')) { // countries > country, industries > industry...
        let m2m_name = name.slice(0, -3) + 'y'
        if (model_names[m2m_name] !== undefined)
        return {type: 'ManyToManyField', relation: model_names[m2m_name]}
    }
    return null
}



export function guess_type(name, store) {
    // tries to guess a type by name (returns dict(type, relation))
    let result = guess_common_names(name)
    if (result !== null) {
        return {type: result, relation: null}
    }
    
    result = guess_relational(name, store)
    if (result !== null) {
        return result
    }
    
    // by default we put it as charfield as seems the most common case
    return {type: 'CharField', relation: null}
}
