import { useEffect, useState } from 'react'
import ReactMarkdown from 'react-markdown'
import post1 from './post1.md'

const MyComponent = () => {
    const [text, setText] = useState('')

    useEffect(() => {
        fetch(post1)
            .then((response) => response.text())
            .then((md) => {
                setText(md)
            })
    }, [])

    return (
        <div>
            <ReactMarkdown children={text} />
        </div>
    )
}

export default MyComponent