import { useEffect, useState } from 'react'
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Markdown from './Markdown';
import post1 from './post1.md';

interface MainProps {
    title: string;
}

export default function Main(prop: MainProps) {
    const { title } = prop;
    const [text, setText] = useState('')

    useEffect(() => {
        fetch(post1)
            .then((response) => response.text())
            .then((md) => {
                setText(md)
            })
    }, [])

    return (
        <Grid
            item
            xs={12}
            md={8}
            sx={{
                '& .markdown': {
                    py: 3,
                },
            }}
        >
            <Typography variant="h6" gutterBottom>
                {title}
            </Typography>
            <Divider />

            <Markdown className="markdown" key={text.substring(0, 40)}>
                {text}
            </Markdown>

        </Grid>
    );
}