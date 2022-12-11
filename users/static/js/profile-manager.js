'use strict';

const e = React.createElement;

class ProfileManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = { active: true };
  }

  render() {
    if (this.state.active) {
      return 'The profile manager is active.';
    }

    return e(
      'p',
      {},
      'profile'
    );
  }
}

const domContainer = document.querySelector('#profile-manager-container');
const root = ReactDOM.createRoot(domContainer);
root.render(e(ProfileManager));