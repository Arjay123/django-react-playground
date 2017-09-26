var React = require('react')
var ReactDOM = require('react-dom')


class Hello extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            data: [{"test": "test"}]
        }
    }

    load() {
        $.ajax({
            url: "http://localhost:8000/api/persons",
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data.results});
                console.log(data)
            }.bind(this),
            error: function(error){
                this.setState({data: []})
                console.log("error")
            }.bind(this)
        })
    }

    componentDidMount() {
        this.load();
    }

    render() {
        var data_render = <h2>sup</h2>
        if(this.state.data){
            data_render = this.state.data.map((i, j) =>
                <h2>{i.name}</h2>
            );
        }
        else {
            console.log("butts")
        }

        return (
            <div>
                <h1>Hello, React!</h1>
                {data_render}
            </div>
        )
    }
}

ReactDOM.render(<Hello />, document.getElementById('container'))